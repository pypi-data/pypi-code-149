from lxml import etree


def tag_from_event(event, idx):
    time_offset = 4375 # 526
    time_event = time_offset + event["minute"] * 60 + event["second"]
    time_start = time_event - 20                                           # UNSTABLE
    time_end = time_event + 20
    code = "Pass Into Box (For)"

    instance = etree.Element("instance")
    etree.SubElement(instance, "ID").text = str(idx)
    etree.SubElement(instance, "start").text = str(time_start)
    etree.SubElement(instance, "end").text = str(time_end)
    etree.SubElement(instance, "code").text = code
    # print(etree.tostring(instance, pretty_print=True))

    return instance

def generate_tag_xml():
    root = etree.XML("<file><ALL_INSTANCES></ALL_INSTANCES></file>")

    for i in success_pass_events.index:
        event = success_pass_events.loc[i]
        instance = tag_from_event(event, i+1)
        root.append(instance)

    print(etree.tostring(root))
