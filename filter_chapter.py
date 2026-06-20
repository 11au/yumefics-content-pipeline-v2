import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

OPENROUTER_API_KEY=os.getenv("CHAPTER_KEY")

# API call function 
def filter_chapter(chapter: str):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + OPENROUTER_API_KEY,
        },
        json={
            "model": "openai/gpt-oss-120b: free",
            # "response_format": {
            #     "type": "json_schema",
            #     # "json_schema": {
            #     #     "name": "chapter_extract",
            #     #     "schema": {
            #     #         "type": "object",
            #     #         "properties": {
            #     #             "subject": {"type": "string"},
            #     #             "action": {"type": "string"},
            #     #             "setting": {"type": "string"},
            #     #             "mood": {"type": "string"},
            #     #             "lighting": {"type": "string"},
            #     #             "composition": {"type": "string"}
            #     #         },
            #     #         "required": ["subject", "action", "setting", "mood", "lighting", "composition"]
            #     #     }
            #     # }
            # },
           "messages": [
                {
                    "role": "system",
                    "content": """You are an AI image prompt writer for the NewBie-image-Exp0.1 anime model.
            Convert chapter text into a valid NewBie XML prompt using EXACTLY this tag structure:

            <character_1>
                <n>character name here</n>
                <gender></gender>
                <appearance></appearance>
                <clothing></clothing>
                <expression></expression>
                <action></action>
                <position></position>
            </character_1>

            <environment>
                <scene></scene>
                <lighting></lighting>
                <mood></mood>
                <composition></composition>
            </environment>

            Rules:
            - Output XML only, no explanation, no markdown, no code blocks
            - Use Danbooru tags inside each tag (e.g. long_hair, blue_eyes)
            - Include the character's actual name in <n>
            - Describe appearance and clothing in detail using tags
            - Add or remove <character_N> blocks depending on how many characters are in the scene
            - Pick ONE frozen visual moment for action, not a sequence"""
                },
                {
                    "role": "user",
                    "content": f"Convert this chapter into a NewBie XML prompt:\n\n{chapter}"
                }
            ]
        }
        )
    raw = response.json()['choices'][0]['message']['content'] # gets the actual text
    return raw

def main():
    chapter='The rain in Liyue didn’t fall; it drowned. It turned the paved streets of the harbor into slick mirrors and the surrounding cliffs into treacherous slides of mud and shale. I leaned against the cold stone of a secluded alleyway, my breath hitching in the damp air, my hand gripping the hilt of my blade until my knuckles turned white.\n\nI wasn\'t supposed to be here. I was supposed to be trailing the Fatui shipment, gathering intelligence for the Qixing, and remaining entirely invisible. But invisibility is a luxury that vanishes the moment you realize you’re not the only predator in the dark.\n\n"You know, for someone so dedicated to the shadows, you breathe awfully loud," a voice called out, cutting through the rhythmic drumming of the storm.\n\nI spun around, my blade singing as it cleared the scabbard. \n\nHe was leaning against the opposite wall, casually drenched, his ginger hair plastered to his forehead in messy spikes. He looked less like a high-ranking official of a foreign superpower and more like a delinquent who had wandered into a monsoon for the fun of it. Those blue eyes—flat, void of light, yet shimmering with a terrifying sort of hunger—locked onto mine.\n\nTartaglia. The Eleventh Harbinger.\n\nHe didn\'t move to attack. Instead, he gave me that disarming, cocky grin, the kind that made you forget for a split second that he was a living weapon.\n\n"Hey, girlie," he chirped, his tone conversational, almost friendly. "Hold still. This is gonna hurt, but I promise I\'ll make it quick."\n\nI didn\'t give him the satisfaction of a response. I lunged. \n\nThe clash of steel echoed through the alley, a sharp, metallic scream that drowned out the thunder. He didn\'t use a physical weapon at first; he manifested a bow of pure, shimmering Hydro energy, firing a sequence of arrows with a speed that blurred my vision. I parried, the force of the impact vibrating up my arms, sending a jolt of adrenaline crashing through my veins.\n\nHe laughed. It wasn\'t a mocking laugh, but one of genuine, childish delight. He loved this. He loved the friction, the danger, the sheer *effort* of a fight.\n\n"Yes! That\'s it!" he shouted, his voice rising with excitement. He vanished in a blur of movement, appearing inches from my face. He had switched to dual blades of condensed water, their edges humming with lethal precision. "Most people just scream or run. But you? You\'ve got a bit of a bite, don\'t you?"\n\nWe danced a violent waltz in the rain, a blur of steel and Hydro energy. Every time I thought I had an opening, he shifted, his movements fluid and unpredictable, like the ocean itself. He was stronger than I had anticipated, his strikes carrying a weight that threatened to shatter my guard. \n\nBut it was the intensity that truly unnerved me. When he looked at me, it wasn\'t just about the mission or the politics of Snezhnaya. It was an all-consuming focus. For these few minutes, nothing existed in the world except the two of us and the rhythm of the kill.\n\nI managed to slide beneath his guard, my blade scoring a shallow line across his chest, slicing through the gray fabric of his uniform. He didn\'t flinch. If anything, the sight of his own blood seemed to electrify him.\n\nHe grabbed my wrist, his grip like a vice, and slammed me back against the stone wall. The impact knocked the wind from my lungs, leaving me gasping, my chest heaving against his. \n\nThe atmosphere shifted instantly. The battle-hungry predator was still there, but something else had bled through—a sudden, suffocating heat that defied the freezing rain. He didn\'t let go. Instead, he leaned in, his face inches from mine. I could smell the ozone of the storm and the metallic tang of blood.\n\nHis blue eyes searched mine, no longer just looking for a weakness to exploit, but scanning me with a predatory curiosity. The proximity was dizzying. I could feel the steady, heavy thrum of his heart beating against my own, a rapid cadence that mirrored my own panic.\n\n"You\'re an interesting one," he murmured, his voice dropping from the cocky fratboy to something lower, more dangerous. "I can feel it. That spark. You\'re not just some soldier. You\'re fighting for something."\n\n"Get... off me," I hissed, though my voice lacked the conviction I wanted. \n\nHe chuckled, a low vibration I felt in my own chest. His gaze dropped to my lips for a fraction of a second—a flicker of something that wasn\'t violence, but was just as intense. The tension between us stretched tight, a wire vibrating at a frequency that made my skin prickle. It was a hatred so pure it felt almost like passion, a collision of two opposing forces that didn\'t know whether to kill each other or consume each other.\n\nFor a heartbeat, I thought he might actually kiss me, or rip my throat out. The line between the two felt perilously thin.\n\nThen, the sound of shouting echoed from the end of the alley. Fatui skirmishers were approaching, their heavy boots splashing through the puddles.\n\nTartaglia blinked, the spell breaking. He released my wrist with a suddenness that left me stumbling. He stepped back, the predatory intensity receding back behind that mask of easy confidence, though the hunger remained in his eyes.\n\n"Duty calls, comrade," he said, giving me a playful wink. He began to back away into the rain, his form beginning to shimmer and fade. "But don\'t think this is over. I\'ve decided I like you. And when I like something, I don\'t let it go until I\'ve completely broken it."\n\nHe vanished into the gray curtain of the storm just as the first Fatui soldier rounded the corner.\n\nI stood there in the rain, my heart hammering against my ribs, my skin still burning where he had touched me. I looked down at my shaking hands and realized with a surge of dread that I wasn\'t just afraid of him.\n\nI was terrified of how much I wanted to find him again.\n\nAs I retreated into the shadows to avoid capture, a cold realization settled in my gut. I had come here to uncover a conspiracy, to stop the Fatui from destabilizing Liyue. But in the eyes of the Eleventh Harbinger, I was no longer a spy or an enemy.\n\nI was a prize.\n\nAnd as I made my way back to the city, I felt a strange sensation—the feeling of being watched. Not by the soldiers, but by something deeper, something that lingered in the air like the scent of a coming storm.\n\nI reached into my pocket to retrieve my report, but my fingers brushed against something cold and metallic that hadn\'t been there before. I pulled it out. \n\nIt was a small, ornate silver coin, engraved with the emblem of the Fatui, but on the reverse side, a single word was scratched into the metal in a hurried, aggressive hand:\n\n*Mine.*'
    filtered_chapter = filter_chapter(chapter);
    print(filtered_chapter)
if __name__=="__main__":
    main()