#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import rtm_block_coding
reload(sys)
sys.setdefaultencoding('utf-8')

if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('cp932')(sys.stdout) 

if __name__ == '__main__':
    sys.exit(rtm_block_coding.main(sys.argv))
