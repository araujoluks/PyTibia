# 📝 Description

> Tibia Bot api using python and cpu/gpu to get unlocked fps

# 🗺️ MVP Features Status

- ActionBar:
  - Counting slots :heavy_check_mark:
- BattleList:
  - [Getting monsters](battleList/docs/README.md) :heavy_check_mark:
  - [Checking if monster is being attacked](battleList/docs/README.md) :heavy_check_mark:
  - Is attacking any creature :heavy_check_mark:
- Cavebot:
  - Attacking closest creature :heavy_check_mark:
  - Ignoring non target monsters :heavy_check_mark:
  - Resume coordinate :heavy_check_mark:
- Chat:
  - Check if Server Log is selected :warning:
  - Talk to NPC's to trade :warning:
- Equipment:
  - Count cap :warning:
- Loot:
  - Get dead monsters by player :warning:
    - Parse server logs message to get loot notification :warning:
  - Collect loot :warning:
    - When hunting, go to dead monster to collect :warning:
    - Detect container full :warning:
- Healing:
  - Spell :heavy_check_mark:
  - Potion :heavy_check_mark:
- HUD:
  - Getting coordinates(playable area) :heavy_check_mark:
  - Getting Monsters :warning: (needs improvement)
- Radar:
  - Floor level :heavy_check_mark:
  - Tracking coordinates :heavy_check_mark:
- Refill:
  - Deposit items in depot :warning:
  - Detect trade container :warning:
  - Scroll until icon is detected :warning:
  - Buy necessary quantity of icon :warning:
- Status:
  - Getting Life :heavy_check_mark:
  - Getting Mana :heavy_check_mark:

# ⌨ Development

## ⚙ Running the app

```bash
# main file to track basic functions output like(is burning, has helmet equipped, etc)
python main.py

# to test last experiments with mess code
python test.py
```

# 👷 Authors

- [**Lucas Silva**](https://github.com/lucasmonstro) joao.galiano.silva@gmail.com -
  Developer

See also the list of [contributors](../../graphs/contributors) who participated
in this project

# ❤️ Development inspiration

A special thanks to [**Murilo Chianfa**](https://github.com/MuriloChianfa) the owner of [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).  
I started the bot in his honor as it was my inspiration to create the fastest tibia pixel bot using GPU, parallelism and precomputation.

# 📝 License

Copyright © 2021 [**lucasmonstro**](https://github.com/lucasmonstro)  
This project is [MIT](https://opensource.org/licenses/MIT) licensed
