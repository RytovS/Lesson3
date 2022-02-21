from datetime import datetime, timedelta 

current_datetime = datetime.now() 

dt = current_datetime.date() 
print('Сегодня:', dt) 

dt_tomorrow = dt + timedelta(days=1) 
print('Завтра:', dt_tomorrow)

dt_yesterday = dt - timedelta(days=1) 
print('Вчера', dt_yesterday)

dt_ago = dt - timedelta(days=30) 
print('Это было 30 дней назад', dt_ago)
