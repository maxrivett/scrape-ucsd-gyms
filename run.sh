today=`date '+%Y_%m_%d_%H_%M_%S'`; 
git pull --ff-only
python3 index.py
git add .
git commit -m "Pulled data at $today"
git push -u origin main