#!/usr/bin/env python3

#-*- coding: utf-8 -*-
from mrjob.job import MRJob
from mrjob.step import MRStep
import sys 

class MRmaxWomClothinCash(MRJob):
    def mapper(self, _, line):
        splitted_line = line.split("\t")
        if splitted_line[3]=="Women's Clothing" and splitted_line[5]=="Cash":
            yield(splitted_line[2], float(splitted_line[4]))
        
    def reducer_int(self, word, counts):
        yield None, (word,sum(counts))
        
    def reducer_find_max(self, _, pairs):
    # each item of word_count_pairs is (count, word),
    # so yielding one results in key=counts, value=word
        yield max(pairs)

    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer_int),
            MRStep(reducer=self.reducer_find_max)
        ]

if __name__ == '__main__':
    MRmaxWomClothinCash.run()