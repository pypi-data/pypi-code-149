# -*- coding: utf-8 -*-

import logging
import logging.handlers


def init(loglevel=logging.DEBUG, errlevel=logging.ERROR,
         filename='debug', filemode='a'):
    """ init the logger, must be called at first
    """

    logging.basicConfig(
        level=loglevel, filename=filename + '.log', filemode=filemode,
        format='%(asctime)s $%(process)d %(name)s %(levelname)s %(filename)s: #%(lineno)d %(message)s')

    err_handler = logging.FileHandler(filename + '.err')
    err_handler.setLevel(errlevel)
    err_handler.setFormatter(
        logging.Formatter('%(asctime)s $%(process)d %(name)s %(levelname)s %(filename)s: #%(lineno)d %(message)s'))

    logging.getLogger('').addHandler(err_handler)


def debugf(modulename):
    """ debugf wrapper
    """
    return logging.getLogger(modulename).log


def debugm(modulename):
    return logging.getLogger(modulename)
