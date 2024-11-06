import { Users } from './users';

export interface SubTopiqs {
    name: string;
    creatorId: string;
    moderators: string[];
    posts: string[];
    id: string;
}