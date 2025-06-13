from playwright.sync_api import Page
import pytest


def test_drag_and_drop(page: Page):
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("https://jqueryui.com/resources/demos/droppable/default.html")

    draggable = page.locator("#draggable")
    droppable = page.locator("#droppable")

    # Get bounding boxes
    draggable_box = draggable.bounding_box()
    droppable_box = droppable.bounding_box()

    # Move to the center of the draggable element
    page.mouse.move(
        draggable_box["x"] + draggable_box["width"] / 2,
        draggable_box["y"] + draggable_box["height"] / 2
    )

    page.mouse.down()

    # Move to the center of the droppable element
    page.mouse.move(
        droppable_box["x"] + droppable_box["width"] / 2,
        droppable_box["y"] + droppable_box["height"] / 2
    )

    page.mouse.up()

    page.wait_for_timeout(3000)
