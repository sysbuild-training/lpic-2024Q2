#!/usr/bin/python3
# -*- utf-8 -*-
#
# Copyright (C) 2024 Ken'ichi Fukamachi
#   All rights reserved. This program is free software; you can
#   redistribute it and/or modify it under 2-Clause BSD License.
#   https://opensource.org/licenses/BSD-2-Clause
#
# mailto: fukachan@fml.org
#    web: https://www.fml.org/
# github: https://github.com/fmlorg
#
# $FML: rekognition.py,v 1.1 2024/04/06 01:20:55 fukachan Exp $
# $Revision: 1.1 $
#        NAME: rekognition.py
# DESCRIPTION: a simple wrapper in using AWS Rekognition.
#              We support only detectLabels() function since
#              implementation of other functions is left for further exercises:-)
#
import sys
import os
import boto3

def detectLabels(file):
    with open(file, mode="rb") as fp:
        body     = fp.read()
        client   = boto3.client('rekognition','us-east-1')
        response = client.detect_labels(
            Image = {
                'Bytes': body
            }
        )
        return response['Labels']


#
# DEBUG
#
def usage():
    print("Usage: {} FILE(S)".format(sys.argv[0]))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        usage()

    for file in sys.argv[1:]:
        if os.path.exists(file):
            print(">>> {}".format(file))
            r = detectLabels(file)
            print(r)
