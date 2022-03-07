#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob
import sys 

class MRachatcateg(MRJob):
    def mapper(self, _, line):
        for word in [(line.split("\t"))[3]]:
            yield(word, 1)
    def reducer(self, word, counts):
        yield(word, sum(counts))

if __name__ == '__main__':
    MRachatcateg.run()