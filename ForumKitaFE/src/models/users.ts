import { SubTopiqs } from './subTopiq';
import { Posts } from './posts';

export interface Users {
    username: string;
    password: string;
    email: string;
    phone: string;
    posts: string[];
    upVotes: string[];
    downVotes: string[];
    subTopiqs: string[];
}