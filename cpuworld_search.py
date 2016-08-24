#!/usr/bin/env python
"""
cpuworld_search 
search cpu-world.com via intel sspec
Copyright Shadow-X2
based on
search.py - jenni Web Search Module
Copyright 2009-2013, Michael Yanovich (yanovich.net)
Copyright 2013, Edward Powell (embolalia.net)
Copyright 2008-2013 Sean B. Palmer (inamidst.com)
Licensed under the Eiffel Forum License 2.

More info:
 * jenni: https://github.com/myano/jenni/
 * Phenny: http://inamidst.com/phenny/
"""

import json
import re
import urllib
import web
from modules import proxy

def cpuworld(jenni, input):
    proc_type = re.compile('Processor Type.*<\/td>')
    sspec = re.compile('"\/sspec.*"')
    proc_num = re.compile('Processor number.*<\/td>')
    proc_speed = re.compile('Processor speed.*<\/td>')
    proc_core_cnt = re.compile('Cores.*<\/td>')
    proc_step = re.compile('Core Stepping.*<\/td>')
    proc_core = re.compile('Processor core.*<\/td>')

    if not input.group(2):
        return jenni.reply("No search term.")
    query = input.group(2).encode('utf-8')
    #query = input.group(2)
    jenni.say("first query: '%s' " % query)

    base = 'http://www.cpu-world.com/cgi-bin/IdentifyPart.pl?PART='
    page = web.get(base + query)
    jenni.say("base+query " + base + query)
    jenni.say(page)

    proc_length = len(input.group(2))
    jenni.say(str(proc_length))
    if (proc_length < 4 or proc_length > 5):
        return jenni.reply("Enter Intel sSpec") 

    proc_type_results = proc_type.findall(page)
     
    if proc_type_results:
        proc_type_result = proc_type_results[0]
        proc_type_result = proc_type_result.rstrip('</td>')
        proc_type_result = proc_type_result.replace("</td><td>", ":")

        proc_num_results = proc_num.findall(page)
 
        if proc_num_results:
             proc_num_result = proc_num_results[0]
             proc_num_result = proc_num_result.rstrip('</td>')
             proc_num_result = proc_num_result.replace("</td><td>", ":")
        else:
            proc_num_result = "Prcoessor number:N/A"   

        proc_speed_results = proc_speed.findall(page)

        proc_speed_result = proc_speed_results[0]
        proc_speed_result = proc_speed_result.rstrip('</td>')
        proc_speed_result = proc_speed_result.replace("</td><td>", ":")

        proc_core_cnt_results = proc_core_cnt.findall(page)

        proc_core_cnt_result = proc_core_cnt_results[0]
        proc_core_cnt_result = proc_core_cnt_result.rstrip('</td>')
        proc_core_cnt_result = proc_core_cnt_result.replace("</td><td>", ":")   

        proc_step_results = proc_step.findall(page)

        proc_step_result = proc_step_results[0]
        proc_step_result = proc_step_result.rstrip('</td>')
        proc_step_result = proc_step_result.replace("</td><td>", ":")

        proc_core_results = proc_core.findall(page)

        proc_core_result = proc_core_results[0]
        proc_core_result = proc_core_result.rstrip('</td>')
        proc_core_result = proc_core_result.replace("</td><td>", ":")

        sspec_results = sspec.findall(page)

        sspec_result = sspec_results[0]
        sspec_result = sspec_result.strip('"')
        jenni.say(proc_type_result + " " + proc_num_result + " " + proc_speed_result + " " + proc_core_cnt_result + " " + proc_step_result + " " + proc_core_result)
        jenni.say("Link: http://www.cpu-world.com%s" % sspec_result)
    else:
      jenni.say("No Cpu Info found")     

    #jenni.say(proc_type_result + " " + proc_num_result + " " + proc_speed_result + " " + proc_core_cnt_result + " " + proc_step_result + " " + proc_core_result)
    #jenni.say("Link:http://www.cpu-world.com%s" % sspec_result)

cpuworld.commands = ['cpu' , 'cpuworld']

if __name__ == '__main__':
    print __doc__.strip()
