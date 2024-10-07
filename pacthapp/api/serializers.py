from rest_framework import serializers

class SystemDataSerializer(serializers.Serializer):
    SystemName = serializers.CharField(max_length=255)
    IPAddress = serializers.IPAddressField()
    OSVersion = serializers.CharField(max_length=255)

    # validation for System name
    def validate_SystemName(self, value):
        if value == "invalid_host":
            raise serializers.ValidationError("This system name is not allowed.")
        return value
