"""
Self-Operating Computer
"""
import argparse
from operate.utils.style import ANSI_BRIGHT_MAGENTA
from operate.operate import main


def main_entry():
    parser = argparse.ArgumentParser(
        description="Run the self-operating-computer with a specified model."
    )
    parser.add_argument(
        "-m",
        "--model",
        help="Specify the model to use",
        required=False,
        default="gpt-4-with-ocr",
    )
    parser.add_argument(
        "--download-video",
        help="URL of the YouTube video to download",
        type=str,
    )
    parser.add_argument(
        "--copy-text",
        nargs=2,
        metavar=('SOURCE_FILE', 'DESTINATION_FILE'),
        help="Copy text from source to destination file",
    )
    parser.add_argument(
        "--fill-form",
        help="URL of the form to fill and upload documents",
        type=str,
    )

    
    parser.add_argument(
    "--scrape-url",
    help="URL to scrape data from",
    type=str,
    required=False
)

    # Add a voice flag
    parser.add_argument(
        "--voice",
        help="Use voice input mode",
        action="store_true",
    )
    
    # Add a flag for verbose mode
    parser.add_argument(
        "--verbose",
        help="Run operate in verbose mode",
        action="store_true",
    )
    
    # Allow for direct input of prompt
    parser.add_argument(
        "--prompt",
        help="Directly input the objective prompt",
        type=str,
        required=False,
    )

    try:
        args = parser.parse_args()
        if args.scrape_url:
        scrape_process(args.scrape_url)
        elif args.download_video:
        download_youtube_video(args.download_video, '/path/to/download')
        elif args.copy_text:
        copy_text(*args.copy_text)
        elif args.fill_form:
        fill_form_and_upload_document(args.fill_form)
        else:
        main(
            args.model,
            terminal_prompt=args.prompt,
            voice_mode=args.voice,
            verbose_mode=args.verbose
        )
    except KeyboardInterrupt:
        print(f"\n{ANSI_BRIGHT_MAGENTA}Exiting...")


if __name__ == "__main__":
    main_entry()
