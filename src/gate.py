import os
import sys

# Adding project root directory to Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

import ast
import argparse
from src.data import DATA
from src.diabetes import eg_bayes
from src.soybean import eg_km
from src.smo import gate20
from src.diabetes_explore_low_frequency_settings import diabetes_explore_low_frequency_settings
import src.config as config
from src.l import l
from src.dist import dist
from src.farapart import far
from src.branch import branch
from src.half import half
from src.tree import tree
from src.doubletap import doubletap
from src.hw6 import experimentTreatments, generateStats
from src.bins import bins
from src.eg_rules import rules

def coerce(x):
   try : return ast.literal_eval(x)
   except Exception: return x.strip()

def o(x): 
  return x.__class__.__name__ +"{"+ (" ".join([f"{k} : {v} ;" for k,v in sorted(x.items()) if k[0]!="_"]))+"}"

def argument_parser():

    parser = argparse.ArgumentParser(description='Command line options.')
    parser.add_argument('-b', '--bins', type=int, default=16, help='initial number of bins')
    parser.add_argument('-B', '--Bootstraps', type=int, default=512, help='number of bootstraps')
    parser.add_argument('-c', '--cohen', type=float, default=.35, help='parametric small delta')
    parser.add_argument('-C', '--Cliffs', type=float, default=.2385, help='non-parametric small delta')
    parser.add_argument('-CC', '--Cut', type=float, default=.1, help='ignore ranges less than C*max')
    parser.add_argument('-d', '--d', type=int, default=32, help='frist cut')
    parser.add_argument('-D', '--D', type=int, default=4, help='second cut')
    parser.add_argument('-f', '--file', type=str, default="../data/auto93.csv", help='where to read data')
    parser.add_argument('-F', '--Far', type=float, default=.95, help='distance to  distant rows')
    parser.add_argument('-g', '--go', type=str, default="help", help='start up action')
    parser.add_argument('-H', '--Half', type=int, default=256, help='#examples used in halving')
    parser.add_argument('-p', '--p', type=int, default=2, help='distance coefficient')
    parser.add_argument('-S', '--seed', type=int, default=1234567891, help='random number seed')
    parser.add_argument('-r', '--rest', type=int, default=3, help='|rest| is |best|*rest')
    parser.add_argument('-t', '--todo', type=str, default="help", help='Start up action')
    parser.add_argument('-T', '--Top', type=int, default=10, help='max. good cuts to explore')
    parser.add_argument('-k', '--k', type=int, default=1, help='low class frequency kludge')
    parser.add_argument('-m', '--m', type=int, default=2, help='low attribute frequency kludge')
    parser.add_argument('-BB', '--Beam', type=int, default=10, help='max number of ranges')
    parser.add_argument('-SS', '--Support', type=int, default=2, help='coeffecient on best')

    return parser

class SLOTS(dict): 
  __getattr__ = dict.get
  __setattr__ = dict.__setitem__
  __repr__ = o

def main():
  args = argument_parser().parse_args()
  config.the = SLOTS(__doc__= __doc__, **vars(args))
  if config.the.todo == "stats":
    data = DATA(config.the.file, None)
    getattr(data, config.the.todo)()
  if config.the.todo == "diabetes":
    eg_bayes() 
  if config.the.todo == "diabetes-elfs":
    diabetes_explore_low_frequency_settings()
  if config.the.todo == "soybean":
    eg_km()
  if config.the.todo == "SMO":
    gate20()
  if config.the.todo == "dist":
    dist()
  if config.the.todo == "far":
    far()
  if config.the.todo == "branch":
    branch()
  if config.the.todo == "half":
    half()
  if config.the.todo == "tree":
    tree()
  if config.the.todo == "doubletap":
    doubletap()
  if config.the.todo == "generatestats":
    generateStats()
  if config.the.todo == "experimenttreatments":
    experimentTreatments()
  if config.the.todo == "bin":
    bins()
  if config.the.todo == "rule":
    rules()

if __name__ == "__main__":
  main()
  