run_cmd="cd backend && python -u manage.py runserver 0.0.0.0:8000  > ../log_server.log 2>&1"
run_cmd+="& cd backend && python -u manage.py worker > ../log_worker.log 2>&1"
nohup sh -c "$run_cmd" &