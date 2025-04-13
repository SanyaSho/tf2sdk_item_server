# TF2SDK Item Server

> [!CAUTION]
> This software was created in educational purposes and it's against Valve's TOS.

Simple inventory manager for [TF2SDK](https://www.teamfortress.com/post.php?id=238809)

## How to use?
### SERVER-SIDE
1. Generate the protobuf messages using the `./comp_proto.sh` script. 
2. Generate and enter an venv using the `python -m venv .venv` and `source .venv/Scripts/activate` (Windows, Git-Bash) / `source .venv/bin/activate` (Linux) commands.
3. Install required packages using `pip install -r requirements.txt`.
4. Add your SteamID and AccountID to the `scripts/player_info.json` file. You can get both of them using [SteamDB](https://steamdb.info).
5. Run a webserver using the `./run_webserver.sh` script.
### CLIENT-SIDE
1. Open the [tf_gc_client.cpp](https://github.com/ValveSoftware/source-sdk-2013/blob/0759e2e8e179d5352d81d0d4aaded72c1704b7a9/src/game/client/tf/tf_gc_client.cpp#L67) and [tf_gc_server.cpp](https://github.com/ValveSoftware/source-sdk-2013/blob/0759e2e8e179d5352d81d0d4aaded72c1704b7a9/src/game/server/tf/tf_gc_server.cpp#L45) and add `return "http://127.0.0.1:8080/";` into beginning of `GetWebBaseUrl` functions.
2. Recompile client_tf and server_tf.

## Q&A
### Can i use this for my mod on Steam?
No, you can't. This software was written for local servers only.
### Can this software manipulate with my TF2 inventory?
No, this software is not reading/writing any of your TF2's inventory data. It's not even connected to Valve's GC.
### How i can add some new items to my inventory?
It's very simple. See the `CMsgSOCacheSubscribedSerializerTest.py` for various examples.
### I am using my modified version of items_game.txt. How i can add my items using this software?
If you have any custom attributes and you want to get access to them using the attribute by class/name accessor you can just copy your items_game.txt to the `scripts/items/` folder.
Everything else should work as intended.