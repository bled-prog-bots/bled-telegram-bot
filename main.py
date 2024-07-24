import asyncio
import logging
from app import config, logging_config, bot


async def main():
    cfg = config.get_config()

    logging_config.setup(
        log_format=cfg.logging.log_format,
        level=cfg.logging.log_level,
    )

    await bot.start(cfg)


if __name__ == '__main__':
    asyncio.run(main())
