# -*- coding: utf-8 -*-
# @Time    : 2022/3/1 16:17
import typing
import numpy as np
# from ..tokenization import FullTokenizer
# from ..feature import token_ids_decode



_DoneFlag_DONE = 0
_DoneFlag_CAN = 1
_DoneFlag_REDO = 2

# your model need 5 inputs ['input_mask', 'input_type_ids', 'input_word_ids', 'temperature', 'top_k', 'top_p']
def callback_predict_fake(fn_args, b_input_ids,
                          b_input_mask,
                          b_seg_ids,
                          temperature,
                          top_k,
                          top_p):
    output = np.random.randint(670, 7000, size=(*b_input_ids.shape, 21128))
    # results = model_pred.predict(x=inputs)
    return output


def decode(
        text: typing.AnyStr,
        tokenizer,
        fn_predict_call=callback_predict_fake,
        fn_args=None,
        max_length=64,
        temperature=1.0,
        top_k=3,
        top_p=1.0,
        start_tokens: typing.Union[typing.List,typing.Tuple]=('[CLS]',),
        ignore_tokens: typing.Union[typing.List,typing.Tuple]=('[UNK]',),
        end_tokens: typing.Union[typing.List,typing.Tuple]=('[SEP]',),
        num=10,
        max_retrey=3,
):
    assert num > 0
    batch_text_or_tokens = [text] * num
    return batch_decode(batch_text_or_tokens=batch_text_or_tokens,
                        tokenizer=tokenizer,
                        fn_predict_call=fn_predict_call,
                        fn_args=fn_args,
                        max_length=max_length,
                        temperature=temperature,
                        top_k=top_k,
                        top_p=top_p,
                        start_tokens=start_tokens,
                        ignore_tokens=ignore_tokens,
                        end_tokens=end_tokens,
                        max_retrey=max_retrey,
                        )

def callback_token_decode(tokenizer,logit):
    token: str = tokenizer.inv_vocab[logit]
    if tokenizer.basic_tokenizer.do_lower_case:
        token = token.lower()
    if token.startswith('##'):
        token = token[2:]
    if token.endswith('##'):
        token = token[:-2]
    return token

def batch_decode(
        batch_text_or_tokens: typing.List,
        tokenizer,
        fn_predict_call=callback_predict_fake,
        fn_args=None,
        fn_token_decode=callback_token_decode,
        max_length=64,
        temperature=1.0,
        top_k=3,
        top_p=1.0,
        start_tokens: typing.Union[typing.List,typing.Tuple]=('[CLS]',),
        ignore_tokens: typing.Union[typing.List,typing.Tuple]=('[UNK]',),
        end_tokens: typing.Union[typing.List,typing.Tuple] = ('[SEP]',),
        max_retrey=3,
):


    if tokenizer.basic_tokenizer.do_lower_case:
        start_tokens = tuple(_.lower() for _ in start_tokens)
        ignore_tokens = tuple(_.lower() for _ in ignore_tokens)
        end_tokens = tuple(_.lower() for _ in end_tokens)

    b_tokens = []
    for text in batch_text_or_tokens:
        if isinstance(text,str):
            b_tokens.append(list(start_tokens) + tokenizer.tokenize(text))
        else:
            b_tokens.append(list(start_tokens) + list(text))

    bs = len(b_tokens)
    b_input_ids = np.asarray([tokenizer.convert_tokens_to_ids(input_tokens) for input_tokens in b_tokens], dtype=np.int32)
    b_input_mask = np.ones_like(b_input_ids)
    b_seg_ids = np.zeros_like(b_input_ids)
    b_max_retrey = [max_retrey] * bs

    text_results = [[] for _ in range(bs)]
    starts = [len(b_tokens[_]) -1 for _ in range(bs)]
    ends = [max_length-1 for _ in range(bs)]
    flags = []
    for i in range(bs):
        flags.append(_DoneFlag_CAN if starts[i] < ends[i] else _DoneFlag_DONE)
    while any(flags):
        idx_sels = np.asarray(flags, dtype=np.bool)
        batch_preds = fn_predict_call(fn_args,b_input_ids[idx_sels],
                                      b_input_mask[idx_sels],
                                      b_seg_ids[idx_sels],
                                      temperature,
                                      top_k,
                                      top_p)
        if batch_preds is None:
            break
        b_input_ids_one,b_mask_one,b_seg_ids_one = [],[],[]
        for i,idx in enumerate(np.where(idx_sels>0)[0]):
            starts[idx] += 1
            # logits = batch_preds[i, :starts[idx]]
            logits = batch_preds[i:i+1,starts[idx] - 1]
            logits /= temperature
            logits = top_k_logits(logits,top_k)
            logits = top_p_logits(logits,top_p)
            # preds = np.argmax(logits[0],axis=-1)
            # sample_func = lambda p: np.random.choice(len(p), p=p)  # 按概率采样函数
            # preds = np.apply_along_axis(sample_func, 1, logits)[0]
            logits = softmax(logits[0],axis=-1)
            # print(np.where(logits >0))
            # preds = np.random.multinomial(4000, logits , size=1)
            preds = np.random.choice(len(logits), p=logits)

            token = fn_token_decode(tokenizer,preds)
            # tokens = token_ids_decode([preds],tokenizer.inv_vocab)
            # if not tokens:
            #     print(tokens)
            #     tokens = ['[UNK]']
            # token = tokens[0]
            is_ignore_char = False
            if ignore_tokens is not None and token in ignore_tokens:
                b_max_retrey[idx] -= 1
                if b_max_retrey[idx] <= 0:
                    flags[idx] = _DoneFlag_DONE
                else:
                    is_ignore_char = True
                    flags[idx] = _DoneFlag_REDO
                starts[idx] -= 1

            if end_tokens is not None and token in end_tokens:
                is_ignore_char = True
                flags[idx] = _DoneFlag_DONE
                starts[idx] -= 1


            if starts[idx] >= ends[idx]:
                flags[idx] = _DoneFlag_DONE

            if flags[idx] == _DoneFlag_CAN:
                b_input_ids_one.append(preds)
                b_mask_one.append(1)
                b_seg_ids_one.append(1)
            else:
                b_input_ids_one.append(0)
                b_mask_one.append(0)
                b_seg_ids_one.append(0)
            if not is_ignore_char:
                text_results[idx].append(token)

        for i in range(len(b_input_ids)):
            if not idx_sels[i]:
                b_input_ids_one.append(0)
                b_mask_one.append(0)
                b_seg_ids_one.append(0)

        b_input_ids_one = np.expand_dims(np.asarray(b_input_ids_one,dtype=np.int32),axis=1)
        b_mask_one = np.expand_dims(np.asarray(b_mask_one, dtype=np.int32),axis=1)
        b_seg_ids_one = np.expand_dims(np.asarray(b_seg_ids_one, dtype=np.int32),axis=1)

        b_input_ids = np.concatenate((b_input_ids, b_input_ids_one), axis=1)
        b_input_mask = np.concatenate((b_input_mask, b_mask_one), axis=1)
        b_seg_ids = np.concatenate((b_seg_ids, b_seg_ids_one), axis=1)
    return text_results


def top_k_logits(logits, k):
    if k == 0:
        return logits

    values = np.sort(logits)
    min_values = values[:, -k, np.newaxis]
    return np.where(
        logits < min_values,
        np.ones_like(logits, dtype=logits.dtype) * -1e10,
        logits,
    )


def softmax(z,axis=-1):
    t = np.exp(z)
    a = np.exp(z) / np.sum(t, axis=axis,keepdims = True)
    return a

def top_p_logits(logits, p):
    """Nucleus sampling"""
    batch, _ = logits.shape
    sorted_logits = np.sort(logits,axis=-1)
    sorted_logits = sorted_logits[:, ::-1]
    cumulative_probs = np.cumsum(softmax(sorted_logits, axis=1), axis=-1)

    indices = np.stack([
        np.arange(0, batch),
        # number of indices to include
        np.maximum(np.sum(cumulative_probs <= p, axis=-1) - 1, 0),
    ], axis=-1)
    min_values = np.asarray([sorted_logits[tuple(indice)] for indice in indices])
    return np.where(
        logits < min_values[:,np.newaxis],
        np.ones_like(logits) * -1e10,
        logits,
    )