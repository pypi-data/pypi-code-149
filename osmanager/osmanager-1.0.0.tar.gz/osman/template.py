{
    "_source": {
        "includes": []
    },
    "from": "{{from}}{{^from}}0{{/from}}",
    "size": "{{size}}{{^size}}20{{/size}}",
    "sort": {},
    "query": {
        "bool": {
            "must" : [],
            "filter": [],
            "must_not": [],
            "should": []
        }
    }
                                  
}

painless_script = """
            int multiplier = params.multiplier;
            int total = 0;
            for (int i = 0; i < doc['container'].length; ++i) {
                total += doc['container'][i] * multiplier;
            }
            if (total > 7) {
                return true;
            } else {
                return false;
            }
            """

class ScriptGenerator(object):

    def generate_search_template(self):
