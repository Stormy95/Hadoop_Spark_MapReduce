#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob
import sys 

class MRsommeSFmoyen(MRJob):
    def mapper(self, _, line):
        splitted_line=line.split("\t")
        if splitted_line[2]=="San Francisco":
            yield(splitted_line[-1], float(splitted_line[4]))
    def reducer(self, word, counts):
        yield(word,sum(counts))

if __name__ == '__main__':
    MRsommeSFmoyen.run()

