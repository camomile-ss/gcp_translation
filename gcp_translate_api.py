#!/usr/bin/python
# coding: utf-8
# import six
from google.cloud import translate_v2 as translate


def gcp_translate_text(text):
    translate_client = translate.Client()
    try:
        result = translate_client.translate(text, target_language="ja")
    except Exception:
        return "* translate err *"
    return result["translatedText"]


def gcp_translate_texts(texts):
    return [gcp_translate_text(x) for x in texts]
