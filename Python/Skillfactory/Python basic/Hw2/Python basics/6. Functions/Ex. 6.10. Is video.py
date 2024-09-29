'''
Дан словарь data, содержащий в себе несколько вложенных структур данных.
Некоторые из них (независимо от вложенности) содержат ключ "videoID". Значениями для таких ключей являются идентификаторы видео.
Напишите рекурсивную функцию find_video(), которая извлекает все значения с ключом "videoID".
Функция должна принимать на вход словарь data и возвращать список из найденных идентификаторов видео.
Например, при вызове функции для следующего словаря:

data = {
    "type": "video",
    "videoID": "vid001",
    "links": [
        {"type":"video", "videoID":"vid002", "links":[]},
        {   "type":"video",
            "videoID":"vid003",
            "links": [
            {"type": "video", "videoID":"vid004"},
            {"type": "video", "videoID":"vid005"},
            ]
        },
        {"type":"video", "videoID":"vid006"},
        {   "type":"video",
            "videoID":"vid007",
            "links": [
            {"type":"video", "videoID":"vid008", "links": [
                {   "type":"video",
                    "videoID":"vid009",
                    "links": [{"type":"video", "videoID":"vid010"}]
                }
            ]}
        ]},
    ]
}
'''
def find_video(data):
    video_ids = []

    # Если data является словарем
    if isinstance(data, dict):
        # Если есть ключ "videoID", добавляем его значение в список
        if "videoID" in data:
            video_ids.append(data["videoID"])

        # Рекурсивно обрабатываем все значения словаря
        for key, value in data.items():
            video_ids.extend(find_video(value))

    # Если data является списком
    elif isinstance(data, list):
        # Рекурсивно обрабатываем все элементы списка
        for item in data:
            video_ids.extend(find_video(item))

    return video_ids

