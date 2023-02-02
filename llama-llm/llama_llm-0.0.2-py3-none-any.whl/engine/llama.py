from llama.specification.specification import Spec

from powerml import PowerML

from docstring_parser import parse

# TODO: confirm what cue works best for lists
LIST_CUE = "\n-"
ESC_LIST_CUE = "\\n-"
# LIST_CUE = '['
# LIST_CUE = '1.'

SEPARATOR = "\n"


class Llama:
    def __init__(self, config=None):
        if config is None:
            self.llm = PowerML()
        else:
            self.llm = PowerML(config)

        self.examples = []

    def fit(self, examples: list):
        self.examples = examples

    def run(self, input: Spec, output_spec: Spec):
        prompt = ""
        prompt = add_instruction_to_prompt(prompt, input, output_spec)
        for example in self.examples:
            prompt = add_input_to_prompt(prompt, example["input"])
            prompt = add_output_to_prompt(prompt, output_spec, example["output"])
        prompt = add_input_to_prompt(prompt, input)
        prompt = add_output_to_prompt(prompt, output_spec)
        # print("prompt", prompt)

        result = self.llm.predict(prompt)
        # print("result", result)

        return parse_cue(apply_cue(output_spec) + result, output_spec)


def add_instruction_to_prompt(prompt, input, output_spec):
    parsed_input = parse(input.__doc__)
    parsed_output = parse(output_spec.__doc__)
    prompt = f"Given:{SEPARATOR}"
    for param in parsed_input.params:
        prompt += f"{param.description}{SEPARATOR}"
    prompt += f"Generate:{SEPARATOR}"
    for param in parsed_output.params:
        if param.type_name == 'list':
            prompt += f"{param.description} after '{param.arg_name}:{ESC_LIST_CUE}'{SEPARATOR}" # TODO: figure how not to hardcode this
        else:
            prompt += f"{param.description} after '{param.arg_name}:'{SEPARATOR}"
    return prompt

def add_input_to_prompt(prompt, input):
    parsed = parse(input.__doc__)

    for param in parsed.params:
        prompt += (
            param.description + " is " + get_arg(input, param.arg_name) + SEPARATOR
        )

    return prompt

def add_output_to_prompt(prompt, output_spec, output=None):
    parsed = parse(output_spec.__doc__)
    if output:
        for param in parsed.params:
            if param.type_name == 'list':
                prompt += f"{param.arg_name}:"
                for el in getattr(output, param.arg_name):
                    prompt += f"{LIST_CUE}{el}"
                prompt += SEPARATOR
            else:
                prompt += f"{param.arg_name}: {getattr(output, param.arg_name)}{SEPARATOR}"
    else:
        prompt += apply_cue(output_spec)
    return prompt

def apply_cue(output_spec):
    output_name, output_type = list(output_spec.__annotations__.items())[0]
    if output_type == list:
        cue = f"{output_name}:{LIST_CUE}"
    else:
        cue = f"{output_name}:"
    return cue

def parse_cue(output, output_spec):
    output_values = {}
    remainder = output
    for cue_key, cue_type in reversed(output_spec.__annotations__.items()):
        remainder, _, cue_value = remainder.partition(f"{cue_key}:")
        output_values[cue_key] = parse_output(cue_value, cue_type)
    return output_spec.parse_obj(output_values)

def parse_output(output, output_type):
    if output_type == list:
        output = [el.strip() for el in output.split(LIST_CUE) if len(el.strip()) > 0]
    else:
        output = output_type(output.strip())
    return output

def get_arg(input, name):
    value = input.dict().get(name)
    return str(value)
