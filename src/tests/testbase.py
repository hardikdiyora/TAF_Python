import unittest, os
import logging

class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.getCustomLogger(cls)

    @classmethod
    def tearDownClass(cls):
        pass

    def getCustomLogger(self):
        # Configuring the Logger object which is used by Test class & base
        self.LOG = logging.getLogger(__name__)
        self.LOG.setLevel(logging.INFO)

        # Configuring file handler for the output log file
        if not os.path.exists('test-output'):
            os.makedirs("test-output")
        file_handler = logging.FileHandler('test-output/run.log', 'w')
        self.LOG.addHandler(file_handler)

        # Configuring stream handler for console logs output
        stream_handler = logging.StreamHandler()
        self.LOG.addHandler(stream_handler)

        # Configuring the format of logs to be print
        logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(logger_formatter)
        stream_handler.setFormatter(logger_formatter)

