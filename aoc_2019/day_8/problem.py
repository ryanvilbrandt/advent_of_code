from math import inf


def chunkify(array, chunk_size):
    for i in range(0, len(array), chunk_size):
        yield array[i:i + chunk_size]


def str_to_arrays(s, w, h):
    return list(chunkify(s, w))


def str_to_arrays_turned(s, w, h):
    """ If you want the arrays to go top-down, then left-to-right"""
    return [list(s[i::h]) for i in range(h)]


def str_to_layers(s, w, h):
    return [list(chunkify(chunk, w)) for chunk in chunkify(s, w * h)]


def check_image(s, w, h):
    assert len(s) % (w * h) == 0
    image = str_to_layers(s, w, h)
    least_zero_count = inf
    checksum = 0
    for layer in image:
        zero_count, one_count, two_count = 0, 0, 0
        for row in layer:
            zero_count += row.count("0")
            one_count += row.count("1")
            two_count += row.count("2")
        if zero_count < least_zero_count:
            least_zero_count = zero_count
            checksum = one_count * two_count
    return checksum


def merge_row(base_s, new_s):
    return "".join([new if base == '2' else base for base, new in zip(base_s, new_s)])


def merge_layer(base_layer, new_layer):
    return [merge_row(base_row, new_row) for base_row, new_row in zip(base_layer, new_layer)]


def flatten_layers(layers):
    flattened_layer = layers[0]
    for layer in layers[1:]:
        flattened_layer = merge_layer(flattened_layer, layer)
    return flattened_layer


def flatten_image(image, w, h):
    return flatten_layers(str_to_layers(image, w, h))


def increase_contrast(flattened_image):
    return [row.replace("0", " ").replace("1", "#") for row in flattened_image]
