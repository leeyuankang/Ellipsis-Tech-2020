<template>
    <b-container class='container'>
        <b-row class='word-container' align-v="center">
            <div class='general-container'>
                <div class='para'>
                    <b>Robin Li</b> -- Co-Founder, Chairman and Chief Executive Officer
                </div>
                <div class='para'>
                    Hello, everyone.
                </div>
                <div class='para'>
                    <span id='keypt1' class='annotation'>Baidu's total revenues in the second quarter reached RMB26.0 billion, declining 1% year-over-year versus the 7% decline in the first quarter</span>. Baidu Core contributed to the rebound with the second quarter revenue growing 24% sequentially. Baidu Core's online marketing services has demonstrated steady improvement, since the trough in February, with encouraging recovery across many industries.
                </div>
                <div class='para'>
                    The second quarter, however, was also met with temporary setbacks such as new waves of COVID-19 cases appearing in Beijing and other areas of China, where Level 2 pandemic precautionary measures were again put in place. Fast forward to latter half of July, the situation has been improving since then, as COVID-19 cases subside.
                </div>
                <div class='para'>
                    These positive moves forward coupled with some temporary setbacks, leave us cautiously optimistic about the business climate into the second half. While COVID-19, geopolitical tension, and other phenomenon plaguing the economy may continue to bring about hiccups, the opportunities that AI has presented us are getting more exciting.
                </div>
                <div class='para'>
                    Our foray into in-app search three years ago is proving to redefine how content and services are consumed, and allow Baidu to be a competitive force to enable long-tail SMEs to do business online. <span id='keypt2' class='annotation'> More than two-thirds of Baidu App users are logging in daily, which not only demonstrate user stickiness, but also indicates greater sense of identity and belonging of Baidu’s users </span>. The CPM gap between Baidu App and union traffic continues to widen in-app revenue makes up the majority of search and feed revenue, and daily in-app search queries outgrowing the total search market in China.
                </div>
                <div class='para'>
                    Traditional search through a browser direct users away from Baidu, whereas in-app search aggregates third-party content and services onto our platform for a unique closed loop experience. Users come to Baidu to form relationships with merchants, through follow, messaging, live video, shop and so forth.
                </div>
                <div class='para'>
                    With users remaining on Baidu after the landing page, we are in a better position to improve user insight and provide superior user experience such as verifying the merchants, monitoring the content and services on Baidu for better quality, strengthening Baidu's vertical and community offerings, and enabling users to follow, interact and transact with merchants.
                </div>
                <div class='para'>
                    From the merchant's perspective, our customers no longer rely on Baidu only for traffic. They are able to build a fan base through our building blocks of BJH accounts; Smart Mini Program and Managed Page; and increase interaction with their fan base through live videos, coupon giveaways and closed-loop transactions; and leverage our marketing services platform for conversion improvement, look-a-like targeting, and repeat purchases.
                </div>
                <div class='para'>
                    Baidu's value proposition extending from selling traffic to also provide marketing cloud services to empower merchants, consumer relationship management capabilities makes us more competitive by leveraging Baidu's AI and cloud capabilities. The increasing liveliness of our users, their participation in live broadcasting, e-commerce and other activities provides Baidu an opportunity to leverage our existing traffic to move beyond marketing services, into membership, online games, and other revenue streams.
                </div>
                <div class='para'>
                    Our new AI businesses; Xiaodu Smart devices continue to sell well, despite the current economic situation causing headwind to smartphones and other consumer electronics. Baidu Cloud is leveraging Baidu's leading AI to provide intelligent cloud solutions to enterprises to help them digitize and do more with AI computing.
                </div>
                <div class='para'>
                    <span id='keypt3' class='annotation'>Apollo continues to make advances in autonomous driving and commercialization, particularly in the area of smart transportation, which stands to benefit from the new infrastructure initiative that China is pushing to reignite the economy</span>. iQIYI weathered another COVID-19-impacted quarter with positive growth year-over-year, reinforcing the belief that online entertainment can fare well in difficult economic times.
                </div>

                <b-tooltip target="keypt1" placement="top">
                    Look for trends in a company’s earnings growth. Over time, do the earnings generally increase? If so, it’s a pretty good indication that the company is doing something right. You don’t need to see a dramatic increase for a company to be a good choice, though. Even small, regular improvement over a long period of time can be a positive indicator. However, do note of external factors that may be in play like a pandemic or natural disasters
                </b-tooltip>
                <b-tooltip target='keypt2' placement='top'>
                    Look out for sentences like this that screams customer loyalty. A sticky brand experience helps businesses turn leads into buyers and convert customer into repeat buyer, bringing potential revenue. Also, this shows that the company is sustainable in the long run
                </b-tooltip>
                <b-tooltip target='keypt3' placement='top'>
                    Moving forward. It's important to know what are the company future plans are. If the company don't keep up with it competition, they will become irrelevant and are likely to fade away into obscurity. Thus it is paramount that company are always one step ahead.
                </b-tooltip>
            </div>
        </b-row>
    </b-container>
</template>

<script>

export default {
  name: 'Content',
  data() {
      return {
      }
  }
}
</script>

<style scoped>

.word-container{
    height: 100%;
    
}

.general-container{
    padding: 20px 20px 5px 20px;
    text-align: left;
    padding-bottom: 20px;
    width: 100%;
}

.transcript-title{
    font-size: 30px;
    font-weight: 600;
}

.para{
    margin-bottom: 10px ;
}
.annotation{
    background-color: yellow;
}


</style>
