"""pyspeechgrammar - PySpeechGrammar can be used to parse and convert speech grammar formats."""

__version__ = '0.1.0'
__author__ = 'Buechi Matthias <m.buechi@outlook.com>'
__all__ = []

from pyspeechgrammar import jsgf
from pyspeechgrammar import srgs_xml


def convert_jsgf_string_to_srgs_xml_string(jsgf_string):
    p = jsgf.JSGFParser()
    m = p.parse_string(jsgf_string)

    s = srgs_xml.SRGSXMLParser()
    return s.write_string(m)


def convert_jsgf_to_srgs_xml(jsgf_input_file, srgs_output_file):
    p = jsgf.JSGFParser()
    m = p.parse_from_file(jsgf_input_file)

    s = srgs_xml.SRGSXMLParser()
    return s.write_to_file(m, srgs_output_file)