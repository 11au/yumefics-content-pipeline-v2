from yumeifics_API import generate_sample, poll_sample
from comfyui_API import generateImage, poll_image_response

config = {"config":{"fandomSlug":"genshin-impact","characterSlug":"tartaglia","intimacyLevel":"steamy","pov":"first","storyTones":["dramatic","suspenseful"],"includeTropes":["enemies to lovers"]}}

def main():
    response = generate_sample(config)
    print(response)
    chapter = poll_sample(response["pollUrl"])
    print(chapter)

    
if __name__ == "__main__":
    main()