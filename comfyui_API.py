import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

COMFYUI_URL = os.getenv("COMFYUI_URL");
prompts="""<character_1>
<n>Protagonist</n>
    <gender>female</gender>
    <appearance>long_hair brown_hair wet_hair determined focused</appearance>
    <clothing>leather_armor black_cloak wet_clothes sword</clothing>
    <expression>fierce</expression>
    <action>being_gripped_by_wrist pressed_against_stone_walls rain_splattering</action>
    <position>left</position>
</character_1>
<character_2>
    <n>Tartaglia</n>
    <gender>male</gender>
    <appearance>spiky_hair ginger_hair blue_eyes wet_hair smiling</appearance>
    <clothing>gray_uniform harbinger_uniform wet_clothes black_cape</clothing>
    <expression>cocky_grin</expression>
    <action>holding_wrist leaning_in dual_blades_hydro_glow rain_splash</action>
    <position>right</position>
</character_2>
<environment>
    <scene>rainy_alley stone_wall puddles night storm</scene>
    <lighting>dim_storm_lighting street_lamps reflections</lighting>
    <mood>tense erotic dangerous</mood>
    <composition>close_up side_view focus_on_characters rain_droplets mirrored_pavement</composition>
</environment>"""
def generateImage(prompt):
    with open("Workflow_api.json", "r") as f:
        workflow = f.json()
    
    workflow["3"]["inputs"]["text"] = prompt

    updated_json=json.dump(workflow)

    image_response=requests.post(
        COMFYUI_URL+"/prompt",
        json=updated_json
    )

    if "error" in image_response:
        return ({"error": image_response["error"]})
    else: 
        return image_response["prompt_id"]

def poll_image_response(image_response): 
    while True: 
        if "error" in image_response:
            return image_response
        else: 
            image = requests.get(
               COMFYUI_URL+"/history/"+image_response
            )
            return image
