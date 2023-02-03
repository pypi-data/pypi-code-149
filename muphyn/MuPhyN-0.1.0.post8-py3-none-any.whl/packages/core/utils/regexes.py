# Integer
IntegerRegex = r"^[-+]?[0-9]*$"

# Float with comma as decimal separator
CommaFloatRegex = r"^[-+]?[0-9]*,[0-9]*$"

# Float with point as decimal separator
DotFloatRegex = r"^[-+]?[0-9]*(?:\.[0-9]*)?$"

# Float with comma as decimal separator (Scientific Notation)
CommaScientificNumberRegex = r"^-?[1-9](?:,\d+)?[Ee][-+]?\d+$"

# Float with point as decimal separator (Scientific Notation)
DotScientificNumberRegex = r"^-?[1-9](?:\.\d+)?[Ee][-+]?\d+$"
