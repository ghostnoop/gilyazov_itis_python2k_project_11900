import {createRouter, createWebHistory} from 'vue-router'
import Login from "@/views/Login";
import Home from "@/views/Home";
import Registration from "@/views/Registration";
import NotFound from "@/views/NotFound";
import Main from "@/views/Main";
import Board from "@/views/Board";
import Order from "@/views/Order";
import Point from "@/views/Point";
import Executor from "@/views/Executor";
import Service from "@/views/Service";
import Dispute from "@/views/Dispute";
import Maps from "@/views/Maps";
import store from "../store"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/login', component: Login, name: "Login",
            meta: {
                auth: false
            }
        },
        {
            path: '/', component: Home, name: 'FirstPage',
            meta: {
                auth: false
            }
        },
        {
            path: '/registration', component: Registration, name: 'Registration',
            meta: {
                auth: false
            }
        },
        {
            path: '/orders', component: Order, name: 'Order',
            meta: {
                auth: true
            }
        },
        {
            path: '/points', component: Point, name: 'Point',
            meta: {
                auth: true
            }
        },
        {
            path: '/executors', component: Executor, name: 'Executor',
            meta: {
                auth: true
            }
        },
        {
            path: '/services', component: Service, name: 'Service',
            meta: {
                auth: true
            }
        },
        {
            path: '/disputes', component: Dispute, name: 'Dispute',
            meta: {
                auth: true
            }
        },
        {
            path: '/map', component: Maps, name: 'Maps',
            meta: {
                auth: true
            }
        },
        {
            path: '/logout', component: Login, name: 'Login1',
            meta: {
                auth: false
            }
        },

        {path: '/:notFound(.*)', component: NotFound},
        {
            path: '/main', component: Main, name: "Main",
            meta: {
                auth: true
            }
        },
        {
            path: '/board/:id', component: Board, name: "Board",
            meta: {
                auth: true
            }
        },
    ]
})

router.beforeEach((to, from, next) => {
    const requireAuth = to.meta.auth
    if (requireAuth && store.getters['auth/isAuthenticated']) {
        next()
    } else if (requireAuth && !store.getters['auth/isAuthenticated']) {
        next('/login')
    } else {
        next()
    }
})


export default router
