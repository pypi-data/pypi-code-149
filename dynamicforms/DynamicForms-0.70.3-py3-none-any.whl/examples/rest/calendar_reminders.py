from dynamicforms import fields, serializers
from examples.enum_field import EnumField
from examples.models import CalendarReminder


class RemindersSerializer(serializers.ModelSerializer):
    id = fields.AutoGeneratedField(read_only=False, required=False)
    event = fields.AutoGeneratedField(display=serializers.DisplayMode.SUPPRESS, required=False, write_only=True)
    type = EnumField(CalendarReminder.RType)
    unit = EnumField(CalendarReminder.Unit)

    class Meta:
        model = CalendarReminder
        exclude = ()
