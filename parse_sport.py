from parser.sport import Sport
from db.sport_saver import SportSaver
from broker.generate_tasks import GenerateTasks

# Получение информации по спорту
parsed_data = Sport().run()
# Сохранение информации по спорту
match_ids = SportSaver(parsed_data).save()
# Добавление id матчей в очередь
GenerateTasks(match_ids).run()
