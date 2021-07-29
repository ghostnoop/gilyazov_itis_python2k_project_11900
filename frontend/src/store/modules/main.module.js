import store from "@/store";

export default {
    namespaced: true,
    state() {
        return {
            activeMenu: false,
            teams: []
        }
    },
    mutations: {
        clickMenu(state) {
            state.activeMenu = state.activeMenu !== true;
        },
        getTeams(state) {
            console.log('qqqqqqq')

            fetch(`http://localhost:8000/points/`, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${store.getters['auth/token']}`
                },
                mode: "cors"
            }).then(response => response.json())
                .then(result => {
                    console.log('точки')
                    console.log(result)
                    state.teams = result
                    console.log(state.teams)
                })
        }
    },
    actions: {
        mountTeams({commit, dispatch}) {
            commit('getTeams')
        }
    },
    modules: {},
    getters: {
        teams(state) {
            return state.teams
        }
    }
}
