class Serializer(object):

    def _recursive_serialize(self, obj):
        """
            Recursively serialize a given dictionary object
        """
        assert isinstance(obj, dict)
        for k, v in obj.items():
            if v and not isinstance(v, (str, int, dict)) and isinstance(v, object):
                try:
                    obj[k] = self._recursive_serialize(v.__dict__)
                except AttributeError:
                    obj[k] = v
            else:    
                obj[k] = v
    
        return obj