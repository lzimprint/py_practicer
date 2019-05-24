# -*- coding: utf-8 -*-

def sayHi(name):
  print "sayHi " + name
  return name

class tt:
  def sayHi(self, name):
    print "tt sayHi " + name
    return name

if __name__ == '__main__':
   sayHi('main')
