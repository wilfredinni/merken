import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  // mode: 'history',

  routes: [
    {
      path: '/',
      name: 'articles',
      component: () => import(/* webpackChunkName: "home" */ './views/Home.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {
      path: '/new',
      name: 'new',
      component: () => import(/* webpackChunkName: "new" */ './views/NewArticle.vue')
    },
  ]
})
