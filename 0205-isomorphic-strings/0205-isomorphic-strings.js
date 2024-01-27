/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const s_t = {} 
    const t_s = {}

    for (let i = 0 ; i < t.length; i++){
        if (!(s[i] in s_t) && !(t[i] in t_s)){
            s_t[s[i]] = t[i]
            t_s[t[i]] = s[i]
        }

        if (!s[i] in s_t || !t[i] in t_s) {
            return false
        }

        if (s_t[s[i]] !== t[i] || t_s[t[i]] !== s[i]){
            return false
        }
    }

    return true
};