import utils.core

leftSideArrowsImg = utils.core.loadImgAsArray('actionBar/images/leftSideArrows.png')
rightSideArrowsImg = utils.core.loadImgAsArray('actionBar/images/rightSideArrowsImg.png')


@utils.core.cacheObjectPos
def getLeftSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, leftSideArrowsImg)


@utils.core.cacheObjectPos
def getRightSideArrowsPos(screenshot):
    return utils.core.locate(screenshot, rightSideArrowsImg)
