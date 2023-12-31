from db.initDoc import initDoc
from axns.st import st
from axns.uq import uq
from axns.tc import text
from axns.fd import fd
from axns.cc import cc
from axns.mp import mp
from lib.init import gp, lin
from lib.adv import adv, personas, summarize
from lib.upd import upd
from lib.camp import campaignPost
from lib.campaign.initPrompt import generateInitialPrompt
import openai
import asyncio
from aiohttp import ClientSession
from threading import Thread
from lib.campaign.splitter import splitterTron

parameters = initDoc()

mp = mp()

cc = cc()

uq = uq()

fd = fd()

if cc == False:
    def generate_linkedin_post(parameters):
        post = text(lin(parameters))
        st(uq, post, "inPo")
        return post

    def generate_instagram_post(parameters):
        post = text(gp(parameters))
        st(uq, post, "inPo")
        return post

    async def get_feedback(post, parameters, persona):
        return text(adv(post, parameters, persona))

    async def main():
        post = ""
        if mp == "LinkedIn":
            post = text(lin(parameters))
        elif mp == "Instagram":
            post = text(gp(parameters))
        st(uq, post, "inPo")

        feedback_tasks = []
        for i in range(3):
            feedback_task = asyncio.create_task(get_feedback(post, parameters, personas[i]))
            feedback_tasks.append(feedback_task)

        feedbacks = await asyncio.gather(*feedback_tasks)
        feedback = "\n".join(feedbacks)
        feedback = text(feedback, summarize)
        st(uq, feedback, "inFe")

        for i in range(fd):
            post = text(upd(post, feedback, parameters))
            st(uq, post, "rePo", i + 1)

            feedback_tasks = []
            for j in range(3):
                feedback_task = asyncio.create_task(get_feedback(post, parameters, personas[j]))
                feedback_tasks.append(feedback_task)

            feedbacks = await asyncio.gather(*feedback_tasks)
            feedback = "\n".join(feedbacks)
            feedback = text(feedback, summarize)
            st(uq, feedback, "reFe", i + 1)

        post = text(upd(post, feedback, parameters))
        st(True, post, "fiPo")

    asyncio.run(main())

else:
    async def get_feedback(post, parameters, persona):
        return text(adv(post, parameters, persona))

    async def main():
        campaignPrompt = generateInitialPrompt(mp, parameters, "10")
        campaign = text(campaignPrompt)
        campaignPlan = splitterTron(campaign)
        print(campaignPlan)
        quit()
        post = text(campaignPost(parameters))
        st(uq, post, "inPo")

        feedback_tasks = []
        for i in range(3):
            feedback_task = asyncio.create_task(get_feedback(post, parameters, personas[i]))
            feedback_tasks.append(feedback_task)

        feedbacks = await asyncio.gather(*feedback_tasks)
        feedback = "\n".join(feedbacks)
        feedback = text(feedback, summarize)
        st(uq, feedback, "inFe")

        for i in range(fd):
            post = text(upd(post, feedback, parameters))
            st(uq, post, "rePo", i + 1)

            feedback_tasks = []
            for j in range(3):
                feedback_task = asyncio.create_task(get_feedback(post, parameters, personas[j]))
                feedback_tasks.append(feedback_task)

            feedbacks = await asyncio.gather(*feedback_tasks)
            feedback = "\n".join(feedbacks)
            feedback = text(feedback, summarize)
            st(uq, feedback, "reFe", i + 1)

        st(True, post, "fiPo")

    asyncio.run(main())