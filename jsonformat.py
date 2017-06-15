#!/usr/bin/env python
import optparse
import fileinput
import re
import sys
import json

def parse_args():
  p = optparse.OptionParser(usage="%prog --schema", version="%prog 1.0")
  p.add_option('--schema', help="schema to use, eg: \"$date $hour: _ _ $field\"", type="string")
  p.add_option('--fields', help="extra field to send, eg: \"machine=`ifconfig`\"", type="string")
  p.add_option('--verbose', '-v', help="output line and the results\"", action="store_true")  
  options, arguments = p.parse_args()
  if not options.schema:
    options.schema = ''
  return (options, arguments)
    
class Runner (object):
  def __init__(self, schema, extra_fields):
    reg = re.sub('\$([a-z]*)', "([^\s]*)", schema)
    reg = reg.replace(' ', '\s+').replace('_', '[^\s]*')
    self.reg = reg
    self.extra = extra_fields
    self.fields = re.findall('\$([a-z]*)', schema)

  def process(self, line):
    doc = self.__extract(line)
    doc = self.__merge(doc, self.extra)
    return doc

  def __extract(self, line):
    res = re.search(self.reg, line)
    if res:
      return zip(self.fields, res.groups())

  def __merge(self, obj, fields = ''):
    if obj and fields:
      fields = map((lambda e: e.split('=')), fields.split(','))
      return dict(obj+fields)
    elif obj:
      return dict(obj)
  
if __name__ == '__main__':
  options, arguments = parse_args()
  runner = Runner(options.schema, options.fields)
  for line in sys.stdin.readlines():
    res = runner.process(line)
    if options.verbose:
      print line.strip()
    if res:
      print json.dumps(res)
    elif options.verbose:
      print '{NODATA}'
