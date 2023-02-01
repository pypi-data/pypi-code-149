from llama.specification.specification import Spec

from powerml import PowerML

from docstring_parser import parse

# TODO: confirm what cue works best for lists
LIST_CUE = "-"
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

        output_names = list(output_spec.__annotations__.keys())
        prompt += output_names[0] + ":"

        #print("prompt", prompt)

        result = output_names[0] + ":" + self.llm.predict(prompt)
        #print("result", result)

        return parse_cue(result, output_spec)


def add_instruction_to_prompt(prompt, input, output_spec):
    parsed_input = parse(input.__doc__)
    parsed_output = parse(output_spec.__doc__)
    prompt = f"Given:{SEPARATOR}"
    for param in parsed_input.params:
        prompt += f"{param.description}{SEPARATOR}"
    prompt += f"Generate:{SEPARATOR}"

    output_names = list(output_spec.__annotations__.keys())
    output_types = list(output_spec.__annotations__.values())
    for i, output_type in enumerate(output_types):
        if output_type == list:
            prompt += f"{parsed_output.params[i].description} after '{output_names[i]}:\\n{LIST_CUE}'"
        else:
            prompt += f"{parsed_output.params[i].description} after '{output_names[i]}:'{SEPARATOR}"
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
                prompt += f"{param.arg_name}:{SEPARATOR}"
                for el in getattr(output, param.arg_name):
                    prompt += f"{LIST_CUE}{el}{SEPARATOR}"
            else:
                prompt += f"{param.arg_name}: {getattr(output, param.arg_name)}{SEPARATOR}"
    else:
        output_names = list(output_spec.__annotations__.keys())
        output_types = list(output_spec.__annotations__.values())
        for i, output_type in enumerate(output_types):
            if output_type == list:
                prompt += f"{output_names[i]}: {LIST_CUE}"
            else:
                prompt += f"{output_names[i]}:"
    return prompt


def make_prompt(input, output_spec):
    parsed = parse(input.__doc__)

    prompt = parsed.short_description + SEPARATOR
    for param in parsed.params:
        prompt += (
            param.description + " is " + get_arg(input, param.arg_name) + SEPARATOR
        )

    parsed = parse(output_spec.__doc__)
    prompt += f"{SEPARATOR}Generate {parsed.short_description}{SEPARATOR}"

    return prompt


def apply_cue(input, output_spec):
    parsed = parse(output_spec.__doc__)
    output_names = list(output_spec.__annotations__.keys())
    output_types = list(output_spec.__annotations__.values())
    for i, output_type in enumerate(output_types):
        if output_type == list:
            input += f"with {parsed.params[i].description} after '{output_names[i]}:\\n{LIST_CUE}'"
        else:
            input += f"with {parsed.params[i].description} after '{output_names[i]}:'{SEPARATOR}"

    input += output_names[0] + ":"

    return input


def parse_cue(output, output_spec):
    if len(output_spec.__fields__) == 1:
        output_type = list(output_spec.__annotations__.values())[0]
        if output_type == list:
            output = [el.strip() for el in output.split(LIST_CUE)]
        else:
            output = output_type(output.strip())
        return output
    else:
        output_values = {}
        remainder = output
        for cue_key, cue_type in reversed(output_spec.__annotations__.items()):
            remainder, _, cue_value = remainder.partition(f"{cue_key}:")
            cue_value = cue_value.strip()
            if cue_type is list:
                cue_value = [
                    el.strip()
                    for el in cue_value.split(LIST_CUE)
                    if len(el.strip()) > 0
                ]
            output_values[cue_key] = cue_value
        return output_spec.parse_obj(output_values)


def get_arg(input, name):
    value = input.dict().get(name)
    return str(value)
