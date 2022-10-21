import requests
from bs4 import BeautifulSoup
import csv


def get():
    """_summary_
    金沢市のHPからごみ情報を取得
    Returns:
        _type_: _description_
    """
    url = "https://www4.city.kanazawa.lg.jp/soshikikarasagasu/gomigenryosuishinka/gyomuannai/1/3/2/3682.html"

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html.parser")

    dataList = []

    td1 = ""
    rowSpan1 = 0
    td2 = ""
    rowSpan2 = 0
    td3 = ""
    rowSpan3 = 0
    td4 = ""

    divList = soup.find_all("div", class_="wysiwyg")

    if divList != None:
        for div in divList:
            table = div.find('table')
            if table != None:
                tbody = table.find('tbody')
                if tbody != None:
                    trList = tbody.find_all('tr')
                    for tr in trList:
                        if tr != None:
                            tdList = tr.find_all('td')
                            if len(tdList) == 4:
                                if rowSpan1 == 0:
                                    if tdList[0].get('rowspan') != None:
                                        rowSpan1 = int(
                                            tdList[0].get('rowspan')) - 1
                                    else:
                                        rowSpan1 = 0
                                    td1 = tdList[0].text
                                else:
                                    rowSpan1 -= 1

                                if rowSpan2 == 0:
                                    if tdList[1].get('rowspan') != None:
                                        rowSpan2 = int(
                                            tdList[1].get('rowspan')) - 1
                                    else:
                                        rowSpan2 = 0
                                    td2 = tdList[1].text
                                else:
                                    rowSpan2 -= 1

                                if rowSpan3 == 0:
                                    if tdList[2].get('rowspan') != None:
                                        rowSpan3 = int(
                                            tdList[2].get('rowspan')) - 1
                                    else:
                                        rowSpan3 = 0
                                    td3 = tdList[2].text
                                else:
                                    rowSpan3 -= 1

                                td4 = tdList[3].text
                            elif len(tdList) == 3:
                                rowSpan1 -= 1

                                if rowSpan2 == 0:
                                    if tdList[0].get('rowspan') != None:
                                        rowSpan2 = int(
                                            tdList[0].get('rowspan')) - 1
                                    else:
                                        rowSpan2 = 0
                                    td2 = tdList[0].text
                                else:
                                    rowSpan2 -= 1

                                if rowSpan3 == 0:
                                    if tdList[1].get('rowspan') != None:
                                        rowSpan3 = int(
                                            tdList[1].get('rowspan')) - 1
                                    else:
                                        rowSpan3 = 0
                                    td3 = tdList[1].text
                                else:
                                    rowSpan3 -= 1

                                td4 = tdList[2].text

                            elif len(tdList) == 2:
                                rowSpan1 -= 1
                                rowSpan2 -= 1

                                if rowSpan3 == 0:
                                    if tdList[0].get('rowspan') != None:
                                        rowSpan3 = int(
                                            tdList[0].get('rowspan')) - 1
                                    else:
                                        rowSpan3 = 0
                                    td3 = tdList[0].text
                                else:
                                    rowSpan3 -= 1

                                td4 = tdList[1].text

                            dataList.append(
                                [td1.strip(), td2.strip(), td3.strip(), td4.strip()])

    return dataList


def output(dataList):
    """_summary_
    csvファイルの出力
    Args:
        dataList (_type_): _description_
    """
    if len(dataList) != 0:
        with open('kanazawa_gurbage.csv', 'wt', encoding='utf-8', newline='') as fout:
            writer = csv.writer(fout)
            writer.writerows(dataList)


output(get())
