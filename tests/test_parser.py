import pytest
import typing

import parser_html



def hand_parsed_pele():
    original_files: typing.List[parser_html.File] = []

    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) DVD9 | Лицензия",
                               "20 Мар 19",
                               "/torrent/688991/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-dvd9-licenzija",
                               "http://d.rutor.info/download/688991",
                               "2", "0", "6.19 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) HDRip от MegaPeer | Лицензия",
                               "15 Мар 19",
                               "/torrent/517265/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-hdrip-ot-megapeer-licenzija",
                               "http://d.rutor.info/download/517265",
                               "2", "0", "746.57 MB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip от ExKinoRay | Лицензия",
                               "14 Мар 19",
                               "/torrent/517624/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-ot-exkinoray-licenzija",
                               "http://d.rutor.info/download/517624",
                               "25", "3", "1.46 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip 1080p от селезень | Лицензия",
                               "14 Мар 19",
                               "/torrent/517215/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-1080p-ot-selezen-licenzija",
                               "http://d.rutor.info/download/517215",
                               "11", "2", "9.65 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip от MegaPeer | Лицензия",
                               "14 Мар 19",
                               "/torrent/517350/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-ot-megapeer-licenzija",
                               "http://d.rutor.info/download/517350",
                               "15", "0", "1.46 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip от HQ-ViDEO | iTunes",
                               "23 Янв 18",
                               "/torrent/609063/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-ot-hq-video-itunes",
                               "http://d.rutor.info/download/609063",
                               "4", "2", "2.18 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip 720p от ExKinoRay | iTunes",
                               "13 Авг 16",
                               "/torrent/518603/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-720p-ot-exkinoray-itunes",
                               "http://d.rutor.info/download/518603",
                               "3", "0", "5.04 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip от Kaztorrents | КПК | iTunes",
                               "08 Авг 16",
                               "/torrent/517877/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-ot-kaztorrents-kpk-itunes",
                               "http://d.rutor.info/download/517877",
                               "4", "0", "483.68 MB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) HDRip от Scarabey | iTunes",
                               "07 Авг 16",
                               "/torrent/517790/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-hdrip-ot-scarabey-itunes",
                               "http://d.rutor.info/download/517790",
                               "2", "0", "745.27 MB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) HDRip от Scarabey | iTunes",
                               "06 Авг 16",
                               "/torrent/517584/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-hdrip-ot-scarabey-itunes",
                               "http://d.rutor.info/download/517584",
                               "5", "0", "1.45 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) BDRip 720p | iTunes",
                               "04 Авг 16",
                               "/torrent/517221/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-bdrip-720p-itunes",
                               "http://d.rutor.info/download/517221",
                               "5", "0", "4.65 GB"))
    original_files.append(parser_html.File("Пеле: Рождение легенды / Pelé: Birth of a Legend (2016) HDRip | iTunes",
                               "04 Авг 16",
                               "/torrent/517222/pele-rozhdenie-legendy_pelé-birth-of-a-legend-2016-hdrip-itunes",
                               "http://d.rutor.info/download/517222",
                               "1", "0", "2.05 GB"))
    return original_files


def hand_parsed_rick():
    original_files: typing.List[parser_html.File] = []

    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEBRip-HEVC 2160p | Сыендук",
                               "16 Авг 20",
                               "/torrent/770850/rik-i-morti_rick-and-morty-s04-2019-webrip-hevc-2160p-syenduk",
                               "http://d.rutor.info/download/770850",
                               "27", "6", "7.65 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S03] (2017) WEBRip-HEVC 2160p | Сыендук",
                                   "16 Авг 20",
                                   "/torrent/770848/rik-i-morti_rick-and-morty-s03-2017-webrip-hevc-2160p-syenduk",
                                   "http://d.rutor.info/download/770848",
                                   "8", "2", "7.46 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S02] (2015) WEBRip-HEVC 2160p | Сыендук",
                                   "16 Авг 20",
                                   "/torrent/770796/rik-i-morti_rick-and-morty-s02-2015-webrip-hevc-2160p-syenduk",
                                   "http://d.rutor.info/download/770796",
                                   "9", "4", "7.38 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S01] (2013-2014) WEBRip-HEVC 2160p | Сыендук",
                                   "16 Авг 20",
                                   "/torrent/770794/rik-i-morti_rick-and-morty-s01-2013-2014-webrip-hevc-2160p-syenduk",
                                   "http://d.rutor.info/download/770794",
                                   "21", "2", "7.93 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S01-04] (2013-2020) BDRip, WEB-DLRip | Сыендук",
                                   "05 Июн 20",
                                   "/torrent/439034/rik-i-morti_rick-and-morty-s01-04-2013-2020-bdrip-web-dlrip-syenduk",
                                   "http://d.rutor.info/download/439034",
                                   "143", "94", "14.48 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEB-DL 1080p | Сыендук",
                                   "02 Июн 20",
                                   "/torrent/728381/rik-i-morti_rick-and-morty-s04-2019-web-dl-1080p-syenduk",
                                   "http://d.rutor.info/download/728381",
                                   "165", "91", "6.17 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEBRip 1080p | IdeaFilm",
                                   "02 Июн 20",
                                   "/torrent/760796/rik-i-morti_rick-and-morty-s04-2019-webrip-1080p-ideafilm",
                                   "http://d.rutor.info/download/760796",
                                   "16", "12", "10.89 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEBRip 720p | IdeaFilm",
                                   "02 Июн 20",
                                   "/torrent/760795/rik-i-morti_rick-and-morty-s04-2019-webrip-720p-ideafilm",
                                   "http://d.rutor.info/download/760795",
                                   "20", "7", "5.50 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEBRip | IdeaFilm",
                                   "02 Июн 20",
                                   "/torrent/760794/rik-i-morti_rick-and-morty-s04-2019-webrip-ideafilm",
                                   "http://d.rutor.info/download/760794",
                                   "66", "23", "3.40 GB"))
    original_files.append(parser_html.File("Рик и Морти / Rick and Morty [S04] (2019) WEBRip 720p | Сыендук",
                                   "01 Июн 20",
                                   "/torrent/729777/rik-i-morti_rick-and-morty-s04-2019-webrip-720p-syenduk",
                                   "http://d.rutor.info/download/729777",
                                   "149", "68", "3.83 GB"))

    return original_files


@pytest.mark.parametrize("original_files,file_name", [(hand_parsed_pele(), "pele"), (hand_parsed_rick(), "rick")])
def test_parser_pele(original_files, file_name):
    with open(f"tests/{file_name}.html", encoding="utf8") as fh:
        text = fh.read()
    search_files = parser_html.parser_text(text)

    print()
    for i, (search_file, original_file) in enumerate(zip(search_files, original_files), start=1):
        print(i)
        assert search_file.name == original_file.name
        assert search_file.date == original_file.date
        assert search_file.link == original_file.link
        assert search_file.download == original_file.download
        assert search_file.distributions == original_file.distributions
        assert search_file.size == original_file.size
