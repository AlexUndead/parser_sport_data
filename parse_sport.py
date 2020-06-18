from parser.sport import Sport
from db.saver import Saver
from broker.generate_tasks import GenerateTasks

parsed_data = Sport().run()
match_ids = Saver(parsed_data).save()
#GenerateTasks(match_ids).run()
