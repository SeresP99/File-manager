import tkinter as tk


def downscale(img):
    if img.height >= 6000 or img.width >= 6000:
        return downscale_larger_than_6000px(img)
    if img.height >= 5000 or img.width >= 5000:
        return downscale_larger_than_5000px(img)
    if img.height >= 4000 or img.width >= 4000:
        return downscale_larger_than_4000px(img)
    if img.height >= 3000 or img.width >= 3000:
        return downscale_larger_than_3000px(img)
    if img.height >= 2000 or img.width >= 2000:
        return downscale_larger_than_2000px(img)
    if img.height >= 1000 or img.width >= 1000:
        return downscale_larger_than_1000px(img)
    return img


def downscale_larger_than_6000px(img):
    return img.resize((int(img.width * 0.085), int(img.height * 0.085)))


def downscale_larger_than_5000px(img):
    return img.resize((int(img.width * 0.1), int(img.height * 0.1)))


def downscale_larger_than_4000px(img):
    return img.resize((int(img.width * 0.125), int(img.height * 0.125)))


def downscale_larger_than_3000px(img):
    return img.resize((int(img.width * 0.167), int(img.height * 0.167)))


def downscale_larger_than_2000px(img):
    return img.resize((int(img.width * 0.25), int(img.height * 0.25)))


def downscale_larger_than_1000px(img):
    return img.resize((int(img.width * 0.5), int(img.height * 0.5)))


def downscale_to_grid_cell(img, grid):
    grid_width = grid.winfo_width()
    if img.width > grid_width:
        difference = img.width - grid_width
        width_deduction_percent = difference / img.width
        value_to_deduct_from_width = width_deduction_percent * img.width
        value_to_deduct_from_height = width_deduction_percent * img.height
        return img.resize((int(img.width - value_to_deduct_from_width), int(img.height - value_to_deduct_from_height)))

    return img
