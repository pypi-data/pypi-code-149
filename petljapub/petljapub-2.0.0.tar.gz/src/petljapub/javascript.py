from .messages import msg

# javascript support to switching languages in the HTML file
def add_switcher(md, langs, switcher_id=0):
    js_switches = "\n<ul class='language-switcher'>\n"
    for lang in langs:
        js_switches += "<li><a href='javascript:displaySolutionByLanguage(\"{}-{}\", {})'>{}</a></li>\n".format(lang, switcher_id, switcher_id, lang)
    js_switches += "</ul>\n\n"
    
    js_switcher = '''
        
<script type="text/javascript">
   function displaySolutionByLanguage(lang, switcher_id) {{
      var sol_divs = document.getElementsByClassName("sol");
      for (var i = 0; i < sol_divs.length; i++)
             if (sol_divs[i].id.endsWith(switcher_id.toString()))
                  sol_divs[i].style.display = "none";
      document.getElementById("sol-" + lang).style.display = "block";
   }}
   displaySolutionByLanguage(\"{}-{}\", {})
</script>

    '''.format(langs[0], switcher_id, switcher_id)
        
    return js_switches + md + js_switcher

def div(md, lang, switcher_id=0):
    return "<div id='sol-{}-{}' class='sol'>\n{}\n</div>\n".format(lang, switcher_id, md)

def abc_question(spec, question_id=0):
    options = []
    if "multiple" in spec and spec["multiple"]:
        button_type = "checkbox"
    else:
        button_type = "radio"
    
    for answer in spec["answers"]:
        options.append("<input type='{}' name='{}_abc_{}'></input> {}".format(button_type, button_type, question_id, answer))
    
    div = """
<div class='abc' id='abc_{}'>
   <p class='abc_question'>{}</p>
   <p class='abc_answers'>{}</p>
   <p class='abc_button'><input type='button' value='{}' /></p>
   <p class='abc_status'></p>
</div>

<script type="text/javascript">
    var div_abc_{} = document.getElementById('abc_{}');
    var button = div_abc_{}.getElementsByClassName("abc_button")[0];
    button.addEventListener("click", function() {{ 
        var p_answers = div_abc_{}.getElementsByClassName("abc_answers")[0];
        var p_status = div_abc_{}.getElementsByClassName("abc_status")[0];
        var buttons = p_answers.getElementsByTagName("input");
        var given_answers = [];
        for (var i = 0; i < buttons.length; i++)
            if (buttons[i].checked)
               given_answers.push(String.fromCharCode("a".charCodeAt(0) + i));
        if (JSON.stringify(given_answers).replace(/"/g, "'") == "{}")
            p_status.innerHTML = "OK";
        else 
            p_status.innerHTML = "NOT OK";
    }});
</script>
"""
    return div.format(question_id, spec["question"], "\n".join(options), msg("CHECK"), question_id, question_id, question_id, question_id, question_id, spec["correct"])


def iframe(file_name, title="", height=500):
    if title == None:
        title = ""
    if height == None:
        height = 500
    return "<iframe src='{}' title='{}' style='width: 100%; height: {}px' frameBorder='0'></iframe>".format(file_name, title, height)

