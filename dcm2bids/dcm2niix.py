# -*- coding: utf-8 -*-


import glob
import os
from subprocess import call
from .utils import clean


class Dcm2niix(object):
    """
    """

    def __init__(self, dicom_dir, participant=None, output="dcm2niix-example"):
        self.dicomDir = dicom_dir
        self.participant = participant
        self.output = output
        self.options = "-b y -ba y -z y -f '%f_%p_%t_%s'"
        self.sidecars = []


    @property
    def outputDir(self):
        if self.participant is None:
            return os.path.join(os.getcwd(), "tmp_dcm2bids", self.output)
        else:
            return os.path.join(
                    os.getcwd(), "tmp_dcm2bids", self.participant.prefix)


    def run(self):
        clean(self.outputDir)
        self.execute()
        self.sidecars = glob.glob(os.path.join(self.outputDir, "*.json"))
        self.sidecars.sort()
        return 0


    def execute(self):
        for directory in self.dicomDir:
            commandStr = "dcm2niix {} -o {} {}"
            command = commandStr.format(self.options, self.outputDir, directory)
            call(command, shell=True)

