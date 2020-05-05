comments_block_start = None
    while True:
        try:
            comments_block_start = data.index("%{")
        except ValueError:
            break
        if not comments_block_start is None:
            comments_block_end = data.index("%}")
            data = data.replace(data[comments_block_start : comments_block_end + 2],"")
    data = data.split("§§§")
