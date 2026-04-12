#!/bin/bash
# System Pulse — returns full system health in one shot
echo "{"
echo '"timestamp": "'$(date -Iseconds)'",'

# Services
echo '"services": {'
QC=$(curl -s -o /dev/null -w '{"status":%{http_code},"ms":%{time_total}}' --max-time 3 http://localhost:8020/health 2>/dev/null || echo '{"status":0,"ms":0}')
GOBII=$(curl -s -o /dev/null -w '{"status":%{http_code},"ms":%{time_total}}' --max-time 3 http://localhost:8000/ 2>/dev/null || echo '{"status":0,"ms":0}')
OLLAMA=$(curl -s -o /dev/null -w '{"status":%{http_code},"ms":%{time_total}}' --max-time 3 http://localhost:11434/api/tags 2>/dev/null || echo '{"status":0,"ms":0}')
echo '"qc_api": '$QC','
echo '"gobii": '$GOBII','
echo '"ollama": '$OLLAMA','
echo '"bridge": "alive"'
echo '},'

# Docker containers
DOCKER=$(docker ps --format '{"name":"{{.Names}}","status":"{{.Status}}"}' 2>/dev/null | jq -s '.' 2>/dev/null || echo '[]')
echo '"docker": '$DOCKER','

# Resources
RAM=$(free | awk '/Mem:/{printf "%.0f", $3/$2*100}')
DISK=$(df -h / | awk 'NR==2{print $5}' | tr -d '%')
SWAP=$(free | awk '/Swap:/{if($2>0) printf "%.0f", $3/$2*100; else print "0"}')
LOAD=$(uptime | awk -F'load average: ' '{print $2}')
echo '"resources": {'
echo '"ram_pct": '$RAM','
echo '"disk_pct": '$DISK','
echo '"swap_pct": '$SWAP','
echo '"load": "'$LOAD'"'
echo '},'

# Git
BRANCH=$(cd ~/Quantum-Commander 2>/dev/null && git branch --show-current 2>/dev/null || echo "N/A")
BEHIND=$(cd ~/Quantum-Commander 2>/dev/null && git rev-list HEAD..origin/main --count 2>/dev/null || echo 0)
DIRTY=$(cd ~/Quantum-Commander 2>/dev/null && git status --porcelain 2>/dev/null | wc -l || echo 0)
echo '"qc_repo": {'
echo '"branch": "'$BRANCH'",'
echo '"behind": '$BEHIND','
echo '"dirty": '$DIRTY
echo '}'
echo "}"
