export interface User {
    id: bigint
    discriminator: number
    username: string
    avatar_hash: string
    banner_hash?: string
    accent_color: number
    is_bot: boolean
    is_system: boolean
    flags: number
    is_mfa_enabled: boolean
    locale: string
    is_verified: boolean
    email: string
    premium_type: number

}
